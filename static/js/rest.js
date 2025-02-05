document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('searchForm');
    const resultsDiv = document.getElementById('results');
  
    searchForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const searchType = document.getElementById('searchType').value;
      const searchInput = document.getElementById('searchInput').value;
      if (!searchType) {
        alert('Please select a search type');
        return;
      }
      try {
        let url;
        if (searchInput.trim() === '') {
          // If empty, return all books – note that we add a dedicated endpoint below.
          url = '/book';
        } else if (searchType === 'books') {
          url = `/books/${searchInput}`;
        } else {
          url = `/authors/${encodeURIComponent(searchInput)}`;
        }
        const response = await fetch(url);
        const data = await response.json();
        if (!data || (Array.isArray(data) && data.length === 0)) {
          alert('No books found');
          return;
        }
        displayBooks(Array.isArray(data) ? data : [data]);
      } catch (error) {
        console.error('Error:', error);
        alert('Error searching for books');
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
          ${book.status !== 'borrowed' ? `<button onclick="borrowBook(${book.book_id})">Borrow</button>` : ''}
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
        // Refresh the listing after borrowing
        searchForm.dispatchEvent(new Event('submit'));
        return true;
      } catch (error) {
        console.error('Error:', error);
        alert('Error borrowing book');
        return false;
      }
    };
  });
  