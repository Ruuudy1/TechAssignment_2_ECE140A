// In my_library.js

document.addEventListener('DOMContentLoaded', () => {
  const myBooksDiv = document.getElementById('myBooks');

  async function loadMyBooks() {
      try {
          const response = await fetch('/my-inventory');
          const books = await response.json();
          displayMyBooks(books);
      } catch (error) {
          console.error('Error:', error);
          myBooksDiv.innerHTML = '<p>No books currently borrowed</p>';
      }
  }

  function displayMyBooks(books) {
      myBooksDiv.innerHTML = '';
      if (Object.keys(books).length === 0) {
          myBooksDiv.innerHTML = '<p>No books currently borrowed</p>';
          return;
      }
      Object.values(books).forEach(book => {
          const bookElement = document.createElement('div');
          bookElement.className = 'book-container';
          bookElement.dataset.bookId = book.book_id;
          bookElement.innerHTML = `<p>ID: ${book.book_id}</p><p>Title: ${book.title}</p><p>Author: ${book.author}</p><p>Genre: ${book.genre}</p><p>Year: ${book.year}</p><button type="button" onclick="returnBook(${book.book_id})">Return</button>`;
          myBooksDiv.appendChild(bookElement);
      });
  }

  window.returnBook = async (bookId) => {
      try {
          const response = await fetch(`/books/${bookId}`, { method: 'DELETE' });
          if (!response.ok) {
              throw new Error('Failed to return book');
          }
          await loadMyBooks();
      } catch (error) {
          console.error('Error:', error);
          alert('Error returning book');
      }
  };

  loadMyBooks();
});
