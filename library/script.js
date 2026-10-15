const starterBooks = [
  { title: "Wings of Fire", author: "A. P. J. Abdul Kalam", copies: 2 },
  { title: "The Alchemist", author: "Paulo Coelho", copies: 1 },
  { title: "Ikigai", author: "Héctor García and Francesc Miralles", copies: 4 }
];
let books = starterBooks.map(book => ({ ...book }));

const form = document.getElementById("bookForm");
const titleInput = document.getElementById("titleInput");
const authorInput = document.getElementById("authorInput");
const copiesInput = document.getElementById("copiesInput");
const shelf = document.getElementById("shelf");
const message = document.getElementById("message");

function findBook(title) {
  const normalizedTitle = title.trim().toLowerCase();
  return books.find(book => book.title.toLowerCase() === normalizedTitle);
}
function showMessage(text) { message.textContent = text; }

function addBook(event) {
  event.preventDefault();
  const title = titleInput.value.trim();
  const author = authorInput.value.trim();
  const copies = Number(copiesInput.value);

  if (!title || !author) {
    showMessage("Please enter both a title and an author.");
    return;
  }
  if (!Number.isInteger(copies) || copies < 1 || copies > 999) {
    showMessage("Copies must be a whole number between 1 and 999.");
    return;
  }

  const existing = findBook(title);
  if (existing) {
    if (existing.author.toLowerCase() !== author.toLowerCase()) {
      showMessage("That title already exists with a different author.");
      return;
    }
    existing.copies += copies;
    showMessage(`Added ${copies} copies to "${existing.title}".`);
  } else {
    books.push({ title, author, copies });
    showMessage(`Added "${title}" to the library.`);
  }
  form.reset();
  copiesInput.value = "1";
  draw();
}

function borrowBook(title) {
  const book = findBook(title);
  if (!book) { showMessage("Book not found."); return; }
  if (book.copies <= 0) {
    showMessage(`No copies of "${book.title}" are available.`);
    return;
  }
  book.copies -= 1;
  showMessage(`You borrowed "${book.title}".`);
  draw();
}

function returnBook(title) {
  const book = findBook(title);
  if (!book) { showMessage("Book not found."); return; }
  book.copies += 1;
  showMessage(`You returned "${book.title}".`);
  draw();
}

function draw() {
  shelf.replaceChildren();
  let totalCopies = 0;
  document.getElementById("titleCount").textContent = books.length;

  if (books.length === 0) {
    const empty = document.createElement("p");
    empty.className = "empty";
    empty.textContent = "No books yet. Use the form above to add one.";
    shelf.appendChild(empty);
  }

  for (const book of books) {
    totalCopies += book.copies;
    const card = document.createElement("article");
    card.className = "book";
    const title = document.createElement("h3");
    title.textContent = book.title;
    const author = document.createElement("p");
    author.className = "author";
    author.textContent = `by ${book.author}`;
    const count = document.createElement("p");
    count.className = "count";
    count.textContent = `${book.copies} available`;
    const actions = document.createElement("div");
    actions.className = "actions";

    const borrowButton = document.createElement("button");
    borrowButton.type = "button";
    borrowButton.textContent = "Borrow";
    borrowButton.disabled = book.copies === 0;
    borrowButton.addEventListener("click", () => borrowBook(book.title));

    const returnButton = document.createElement("button");
    returnButton.type = "button";
    returnButton.className = "secondary";
    returnButton.textContent = "Return";
    returnButton.addEventListener("click", () => returnBook(book.title));

    actions.append(borrowButton, returnButton);
    card.append(title, author, count, actions);
    shelf.appendChild(card);
  }
  document.getElementById("copyCount").textContent = totalCopies;
}

form.addEventListener("submit", addBook);
document.getElementById("resetButton").addEventListener("click", () => {
  books = starterBooks.map(book => ({ ...book }));
  showMessage("Demo reset to the starter books.");
  draw();
});
draw();
