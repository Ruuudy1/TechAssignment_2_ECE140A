document.addEventListener('DOMContentLoaded', () => {
    const myBooksDiv = document.getElementById('myBooks');

    async function loadMyBooks() {
        try {
            const response = await fetch('/my-inventory');
            if (!response.ok) {
                throw new Error('Failed to fetch inventory');
            }
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
            bookElement.innerHTML = `
                <p><strong>ID:</strong> ${book.book_id}</p>
                <p><strong>Title:</strong> ${book.title}</p>
                <p><strong>Author:</strong> ${book.author}</p>
                <p><strong>Genre:</strong> ${book.genre}</p>
                <p><strong>Year:</strong> ${book.year}</p>
                <button onclick="returnBook(${book.book_id})">Return</button>
            `;
            myBooksDiv.appendChild(bookElement);
        });
    }

    window.returnBook = async (bookId) => {
        if (!bookId) return;
        
        try {
            const response = await fetch(`/books/${bookId}`, {
                method: 'DELETE'
            });
            if (!response.ok) {
                throw new Error('Failed to return book');
            }
            await loadMyBooks();
        } catch (error) {
            console.error('Error:', error);
        }
    };

    loadMyBooks();
});
