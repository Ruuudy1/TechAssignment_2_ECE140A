document.addEventListener('DOMContentLoaded', () => {
  const searchForm = document.getElementById('searchForm');
  const resultsDiv = document.getElementById('results');
  searchForm.addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent any page navigation.
    const searchType = document.getElementById('searchType').value;
    const searchInput = document.getElementById('searchInput').value;
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

    // Save current results so that if no valid results are returned,
    // the page content remains unchanged.
    const originalContent = resultsDiv.innerHTML;

    try {
      const response = await fetch(url);
      if (response.status !== 200) {
        alert(`Error: Endpoint ${url} returned status ${response.status}`);
        return;
      }
      const data = await response.json();
      // For nonempty search, if no results, restore original content.
      if (searchInput.trim() !== "" && (!data || (Array.isArray(data) && data.length === 0))) {
        resultsDiv.innerHTML = originalContent;
        return;
      }
      // Otherwise display the retrieved books.
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
      bookElement.innerHTML = `
        <p>ID: ${book.book_id}</p>
        <p>Title: ${book.title}</p>
        <p>Author: ${book.author}</p>
        <p>Genre: ${book.genre}</p>
        <p>Year: ${book.year}</p>
        <p class="status">Status: ${book.status}</p>
        ${book.status !== 'borrowed' 
          ? `<button type="button" onclick="borrowBook(${book.book_id})">Borrow</button>`
          : `<button type="button" disabled>Borrowed</button>`}
      `;
      resultsDiv.appendChild(bookElement);
    });
  }

  window.borrowBook = async (bookId) => {
    try {
      const response = await fetch(`/books/${bookId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' }
      });
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || 'Failed to borrow book');
      }
      // Update the affected book block without reloading the entire page.
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
