package main
// main package
import (
    "fmt"
    "html/template"
    "math/rand"
    "net/http"
    "time"
)

// HTML template for the web page
const htmlTemplate = `
<!DOCTYPE html>
<html>
<head>
    <title>Random Number Generator</title>
    <script>
        function getRandomNumber() {
            fetch('/random')
            .then(response => response.text())
            .then(data => {
                document.getElementById("result").innerText = "Random Number: " + data;
            });
        }
    </script>
</head>
<body>
    <h1>Click the button to generate a random number</h1>
    <button onclick="getRandomNumber()">Generate</button>
    <p id="result"></p>
</body>
</html>
`

func main() {
    rand.Seed(time.Now().UnixNano())

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        tmpl := template.New("index")
        tmpl, _ = tmpl.Parse(htmlTemplate)
        tmpl.Execute(w, nil)
    })

    http.HandleFunc("/random", func(w http.ResponseWriter, r *http.Request) {
        randomNumber := rand.Intn(100) + 1
        fmt.Fprintf(w, "%d", randomNumber)
    })

    fmt.Println("Server is running on port 8080...")
    http.ListenAndServe(":8080", nil)
}
