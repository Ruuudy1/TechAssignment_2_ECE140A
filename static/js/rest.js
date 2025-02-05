document.addEventListener('DOMContentLoaded', () => {
    const resultsDiv = document.getElementById('results');

    window.searchBooks = async () => {
        const searchType = document.getElementById('searchType').value;
        const searchInput = document.getElementById('searchInput').value;

        try {
            let url;
            if (!searchInput.trim()) {
                url = '/book';  // endpoint for all books
            } else if (searchType === 'Book ID') {
                url = `/books/${searchInput}`;
            } else if (searchType === 'Author') {
                url = `/authors/${encodeURIComponent(searchInput)}`;
            }

            const response = await fetch(url);
            const data = await response.json();
            displayBooks(Array.isArray(data) ? data : [data]);
        } catch (error) {
            resultsDiv.innerHTML = '<p>Error searching for books</p>';
        }
    };

    function displayBooks(books) {
        resultsDiv.innerHTML = '';
        books.forEach(book => {
            const bookDiv = document.createElement('div');
            bookDiv.className = 'book-container';
            bookDiv.innerHTML = `
                <p>ID: ${book.book_id}</p>
                <p>Title: ${book.title}</p>
                <p>Author: ${book.author}</p>
                <p>Genre: ${book.genre}</p>
                <p>Year: ${book.year}</p>
                <p>Status: ${book.status}</p>
                ${book.status !== 'borrowed' ? 
                    `<button onclick="borrowBook(${book.book_id})">Borrow</button>` : 
                    ''}
            `;
            resultsDiv.appendChild(bookDiv);
        });
    }

    window.borrowBook = async (bookId) => {
        try {
            const response = await fetch(`/books/${bookId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            
            if (!response.ok) {
                throw new Error('Failed to borrow book');
            }
            
            const data = await response.json();
            searchBooks(); // Refresh the book list
        } catch (error) {
            alert('Error borrowing book');
        }
    };
});
