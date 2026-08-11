import { Router, Request, Response } from "express";
import { Book } from "../models/book";
import { books } from "../data/books";

const router = Router();

let books: Book[] = [
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

router.get("/", (req: Request, res: Response) => {
    res.status(200).json({
        total: books.length,
        books: books
    });
});

router.get("/:id", (req: Request, res: Response) => {

    const id = Number(req.params.id);

    const book = books.find(book => book.id === id);

    if (!book) {
        return res.status(404).json({
            error: "Libro no encontrado"
        });
    }

    res.status(200).json(book);
});

router.post("/", (req: Request, res: Response) => {

    // Verificar que el Content-Type sea JSON
    const contentType = req.headers["content-type"];

    if (!contentType || !contentType.includes("application/json")) {
        return res.status(415).json({
            error: "El cuerpo de la solicitud debe ser JSON"
        });
    }

    const { title, author, year, loaned } = req.body;

    if (!title || !author || !year) {
        return res.status(400).json({
            error: "Los campos title, author y year son obligatorios"
        });
    }

    if (books.length >= 100) {
        return res.status(409).json({
            error: "No se pueden registrar más de 100 libros"
        });
    }

    const newBook: Book = {
        id: books.length > 0
            ? Math.max(...books.map(book => book.id)) + 1
            : 1,

        title: title,
        author: author,
        year: Number(year),
        loaned: loaned === true
    };

    books.push(newBook);

    res.status(201).json({
        message: "Libro agregado correctamente",
        book: newBook
    });
});

router.put("/:id", (req: Request, res: Response) => {

    const id = Number(req.params.id);

    const index = books.findIndex(book => book.id === id);

    if (index === -1) {
        return res.status(404).json({
            error: "Libro no encontrado"
        });
    }

    const { title, author, year, loaned } = req.body;

    books[index] = {
        ...books[index],
        title: title ?? books[index].title,
        author: author ?? books[index].author,
        year: year ?? books[index].year,
        loaned: loaned ?? books[index].loaned
    };

    res.status(200).json({
        message: "Libro actualizado correctamente",
        book: books[index]
    });
});

router.delete("/:id", (req: Request, res: Response) => {

    const id = Number(req.params.id);

    const index = books.findIndex(book => book.id === id);

    if (index === -1) {
        return res.status(404).json({
            error: "Libro no encontrado"
        });
    }

    const deletedBook = books.splice(index, 1)[0];

    res.status(200).json({
        message: "Libro eliminado correctamente",
        book: deletedBook
    });
});

export default router;