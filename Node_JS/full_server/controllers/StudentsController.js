import { readDatabase } from "../utils";

class StudentsController {
    static async getAllStudents(req, res) {
        const database = process.argv[2];
        try {
            const students = await readDatabase(database);
            const fields = Object.keys(students).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
            let output = 'This is the list of our students';

            for (const field of fields) {
                const list = students[field];
                output += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
            }

            res.status(200).send(output);
        } catch (err) {
            res.status(500).send(err.message);
        }
    }

    static async getAllStudentsByMajor(req, res) {
        const database = process.argv[2];
        const { major } = req.params;

        if (major !== 'CS' && major !== 'SWE') {
            res.status(500).send('Major parameter must be CS or SWE');
            return;
        }

        try {
            const students = await readDatabase(database);
            const list = students[major] || [];
            res.status(200).send(`List: ${list.join(', ')}`);
        } catch (err) {
            res.status(500).send(err.message);
        }
    }
}

export default StudentsController;