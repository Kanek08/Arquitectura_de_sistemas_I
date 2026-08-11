import { Book } from "../models/book";

export const books: Book[] = [
    {
        id: 1,
        title: "Clean Code",
        author: "Robert C. Martin",
        year: 2008,
        loaned: false
    },
    {
        id: 2,
        title: "The Pragmatic Programmer",
        author: "Andrew Hunt",
        year: 1999,
        loaned: true
    },
    {
        id: 3,
        title: "Design Patterns",
        author: "Erich Gamma",
        year: 1994,
        loaned: false
    }
];