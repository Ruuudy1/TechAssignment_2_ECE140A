document.addEventListener('DOMContentLoaded', () => {
    const myBooksDiv = document.getElementById('myBooks');

    async function loadMyBooks() {
        try {
            const response = await fetch('/my-inventory');
            const books = await response.json();
            displayMyBooks(books);
        } catch (error) {
            console.error('Error:', error);
        }
    }

    function displayMyBooks(books) {
        myBooksDiv.innerHTML = '';
        Object.values(books).forEach(book => {
            const bookElement = document.createElement('div');
            bookElement.className = 'book-container';
            bookElement.innerHTML = `
                <p>ID: ${book.book_id}</p>
                <p>Title: ${book.title}</p>
                <p>Author: ${book.author}</p>
                <p>Genre: ${book.genre}</p>
                <p>Year: ${book.year}</p>
                <button onclick="returnBook(${book.book_id})">Return</button>
            `;
            myBooksDiv.appendChild(bookElement);
        });
    }

    window.returnBook = async (bookId) => {
        try {
            const response = await fetch(`/books/${bookId}`, {
                method: 'DELETE'
            });
            if (response.ok) {
                loadMyBooks();
            } else {
                alert('Error returning book');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error returning book');
        }
    };

    loadMyBooks();
});
