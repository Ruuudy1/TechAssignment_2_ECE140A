// In /static/js/rest.js
document.addEventListener('DOMContentLoaded', () => {
  const searchForm = document.getElementById('searchForm');
  const resultsDiv = document.getElementById('results');
  
  searchForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const searchType = document.getElementById('searchType').value;
      const searchInput = document.getElementById('searchInput').value;

      // Choose endpoint based on the (trimmed) search term.
      let url;
      if (searchInput.trim() === "") {
          url = '/book';
      } else if (searchType === 'books') {
          url = `/books/${searchInput}`;
      } else if (searchType === 'authors') {
          url = `/authors/${encodeURIComponent(searchInput)}`;
      } else {
          return;
      }

      // Save the current content so that if query returns no results, the page is unchanged.
      const originalContent = resultsDiv.innerHTML;

      try {
          const response = await fetch(url);
          if (response.status !== 200) {
              alert(`Error: Endpoint ${url} returned status ${response.status}`);
              return;
          }
          const data = await response.json();

          // If nonempty query returns no data, restore original content (thus not changing the page)
          if (searchInput.trim() !== "" && (!data || (Array.isArray(data) && data.length === 0))) {
              resultsDiv.innerHTML = originalContent;
              return;
          }

          // Otherwise, update the page.
          displayBooks(Array.isArray(data) ? data : [data]);
      } catch (error) {
          console.error('Error:', error);
          alert('Error searching for books');
          resultsDiv.innerHTML = originalContent;
      }
  });

  function displayBooks(books) {
      resultsDiv.innerHTML = '';
      books.forEach(book => {
          const bookElement = document.createElement('div');
          bookElement.className = 'book-container';
          bookElement.dataset.bookId = book.book_id;
          bookElement.innerHTML = `<p>ID: ${book.book_id}</p><p>Title: ${book.title}</p><p>Author: ${book.author}</p><p>Genre: ${book.genre}</p><p>Year: ${book.year}</p><p class="status">Status: ${book.status}</p>${book.status !== 'borrowed' ? `<button type="button" onclick="borrowBook(${book.book_id})">Borrow</button>` : `<button type="button" disabled>Borrowed</button>`}`;
          resultsDiv.appendChild(bookElement);
      });
  }

  window.borrowBook = async (bookId) => {
      try {
          const response = await fetch(`/books/${bookId}`, { method: 'PUT', headers: { 'Content-Type': 'application/json' } });
          const data = await response.json();
          if (!response.ok) {
              throw new Error(data.error || 'Failed to borrow book');
          }

          // Instead of reloading the entire search result, update the affected block.
          const bookElement = document.querySelector(`[data-book-id="${bookId}"]`);
          if (bookElement) {
              const btn = bookElement.querySelector('button');
              if (btn) {
                  btn.textContent = 'Borrowed';
                  btn.disabled = true;
              }
              const statusP = bookElement.querySelector('.status');
              if (statusP) {
                  statusP.textContent = 'Status: borrowed';
              }
          }
      } catch (error) {
          console.error('Error:', error);
          alert('Error borrowing book');
      }
  };
});
