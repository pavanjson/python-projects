// quiz/static/quiz/js/quiz_ajax.js
document.addEventListener('DOMContentLoaded', function() {
    const quizForm = document.getElementById('quizForm');
    if (quizForm) {
        quizForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(quizForm);
            fetch(quizForm.action, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                },
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                // Update the result div with the score details
                const resultDiv = document.getElementById('result');
                resultDiv.innerHTML = `
                  <div class="alert alert-info">
                    <h4>Your Score</h4>
                    <p>You answered ${data.score} out of ${data.total} correctly.</p>
                  </div>
                `;
            })
            .catch(error => console.error('Error:', error));
        });
    }
});
