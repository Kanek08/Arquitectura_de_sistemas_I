import express, { Request, Response } from "express";
import booksRouter from "./routes/books.routes";
import { books } from "./data/books";

const app = express();

const PORT = 3000;

app.use(express.json());

app.use("/books", booksRouter);

app.get("/health/fitness", (req: Request, res: Response) => {

    const totalBooks = books.length;

    const loanedBooks = books.filter(
        book => book.loaned === true
    ).length;

    const loanedRatio = totalBooks === 0
        ? 0
        : loanedBooks / totalBooks;

    const loanedPercentage = loanedRatio * 100;

    const capacityHealthy = totalBooks <= 100;

    const loanRatioHealthy = loanedRatio < 0.80;

    const healthy = capacityHealthy && loanRatioHealthy;

    const report = {
        status: healthy ? "Healthy" : "Degraded",

        metrics: {
            totalBooks: totalBooks,
            loanedBooks: loanedBooks,
            availableBooks: totalBooks - loanedBooks,
            loanedPercentage: Number(loanedPercentage.toFixed(2))
        },

        constraints: {
            capacity: {
                limit: 100,
                current: totalBooks,
                healthy: capacityHealthy
            },

            loanRatio: {
                limit: "less than 80%",
                current: `${loanedPercentage.toFixed(2)}%`,
                healthy: loanRatioHealthy
            }
        },

        message: healthy
            ? "La arquitectura cumple con todas las restricciones."
            : "Degradacion de Calidad: una o mas restricciones no se cumplen."
    };

    if (!healthy) {
        return res.status(503).json(report);
    }


    res.status(200).json(report);
});

app.listen(PORT, () => {
    console.log(`Servidor ejecutándose en http://localhost:${PORT}`);
});