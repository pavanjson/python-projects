// quiz/static/quiz/js/dynamic_quiz.js

document.addEventListener('DOMContentLoaded', function() {
    console.log("dynamic_quiz.js loaded");

    let questionCountInput = document.getElementById('question_count');
    let questionsContainer = document.getElementById('questionsContainer');
    let addQuestionBtn = document.getElementById('addQuestionBtn');

    let questionCount = 0;

    function updateQuestionCount() {
        questionCountInput.value = questionCount;
    }

    function createOptionField(questionIndex, optionIndex, optionContainer, optionCountInput) {
        let div = document.createElement('div');
        div.className = 'mb-2 option-field';

        // Option text input
        let input = document.createElement('input');
        input.type = 'text';
        input.name = `option_text_${questionIndex}_${optionIndex}`;
        input.placeholder = `Option ${optionIndex + 1}`;
        input.className = 'form-control d-inline-block';
        input.style.width = '70%';

        // Radio button to mark correct answer
        let radio = document.createElement('input');
        radio.type = 'radio';
        radio.name = `correct_option_${questionIndex}`;
        radio.value = optionIndex;
        radio.className = 'form-check-input ms-2';

        // Delete option button
        let deleteBtn = document.createElement('button');
        deleteBtn.type = 'button';
        deleteBtn.className = 'btn btn-sm btn-danger ms-2';
        deleteBtn.textContent = 'Delete Option';
        deleteBtn.addEventListener('click', function() {
            div.remove();
            // Reorder remaining options
            let optionFields = optionContainer.querySelectorAll('.option-field');
            optionFields.forEach((field, idx) => {
                let textInput = field.querySelector('input[type="text"]');
                textInput.name = `option_text_${questionIndex}_${idx}`;
                let radioInput = field.querySelector('input[type="radio"]');
                radioInput.value = idx;
            });
            optionCountInput.value = optionFields.length;
        });

        div.appendChild(input);
        div.appendChild(radio);
        div.appendChild(deleteBtn);
        return div;
    }

    function createQuestionBlock(questionData) {
        // questionData is optional for editing; if provided, pre-fill fields.
        let questionIndex = questionCount;
        questionCount++;
        updateQuestionCount();

        let block = document.createElement('div');
        block.className = 'card mb-3 question-block';
        block.setAttribute('data-question-index', questionIndex);
        let cardBody = document.createElement('div');
        cardBody.className = 'card-body';

        // Question text input
        let questionLabel = document.createElement('label');
        questionLabel.textContent = `Question ${questionIndex + 1}:`;
        let questionInput = document.createElement('input');
        questionInput.type = 'text';
        questionInput.name = `question_text_${questionIndex}`;
        questionInput.placeholder = 'Enter question text';
        questionInput.className = 'form-control mb-2';
        if (questionData && questionData.question_text) {
            questionInput.value = questionData.question_text;
        }

        // Option container
        let optionContainer = document.createElement('div');
        optionContainer.className = 'option-container mb-2';

        // Hidden input to track number of options for this question
        let optionCountInput = document.createElement('input');
        optionCountInput.type = 'hidden';
        optionCountInput.name = `option_count_${questionIndex}`;
        optionCountInput.value = 0;

        // Button to add an option
        let addOptionBtn = document.createElement('button');
        addOptionBtn.type = 'button';
        addOptionBtn.className = 'btn btn-sm btn-secondary';
        addOptionBtn.textContent = 'Add Option';
        addOptionBtn.addEventListener('click', function() {
            let optionCount = parseInt(optionCountInput.value);
            let optionField = createOptionField(questionIndex, optionCount, optionContainer, optionCountInput);
            optionContainer.appendChild(optionField);
            optionCountInput.value = optionCount + 1;
        });

        // Button to delete the entire question block
        let deleteQuestionBtn = document.createElement('button');
        deleteQuestionBtn.type = 'button';
        deleteQuestionBtn.className = 'btn btn-sm btn-danger ms-2';
        deleteQuestionBtn.textContent = 'Delete Question';
        deleteQuestionBtn.addEventListener('click', function() {
            block.remove();
            // Reorder remaining questions
            let questionBlocks = document.querySelectorAll('.question-block');
            questionCount = 0;
            questionBlocks.forEach((qb) => {
                qb.setAttribute('data-question-index', questionCount);
                let qInput = qb.querySelector(`input[name^="question_text_"]`);
                qInput.name = `question_text_${questionCount}`;
                let optCountInput = qb.querySelector('input[type="hidden"][name^="option_count_"]');
                optCountInput.name = `option_count_${questionCount}`;
                let optionFields = qb.querySelectorAll('.option-field');
                optionFields.forEach((of, idx) => {
                    let textInput = of.querySelector('input[type="text"]');
                    textInput.name = `option_text_${questionCount}_${idx}`;
                    let radioInput = of.querySelector('input[type="radio"]');
                    radioInput.name = `correct_option_${questionCount}`;
                    radioInput.value = idx;
                });
                questionCount++;
            });
            updateQuestionCount();
        });

        cardBody.appendChild(questionLabel);
        cardBody.appendChild(questionInput);
        cardBody.appendChild(optionContainer);
        cardBody.appendChild(optionCountInput);
        cardBody.appendChild(addOptionBtn);
        cardBody.appendChild(deleteQuestionBtn);
        block.appendChild(cardBody);

        // If editing and questionData is provided, load existing options.
        if (questionData && questionData.options) {
            questionData.options.forEach(function(opt, idx) {
                let optionField = createOptionField(questionIndex, idx, optionContainer, optionCountInput);
                let textInput = optionField.querySelector('input[type="text"]');
                textInput.value = opt.text;
                let radioInput = optionField.querySelector('input[type="radio"]');
                radioInput.checked = opt.is_correct;
                optionContainer.appendChild(optionField);
            });
            optionCountInput.value = questionData.options.length;
        }

        return block;
    }

    addQuestionBtn.addEventListener('click', function() {
        let questionBlock = createQuestionBlock();
        questionsContainer.appendChild(questionBlock);
    });

    // If editing an existing quiz, pre-populate questions
    if (typeof existingQuizData !== 'undefined' && Array.isArray(existingQuizData)) {
        existingQuizData.forEach(function(qData) {
            let questionBlock = createQuestionBlock(qData);
            questionsContainer.appendChild(questionBlock);
        });
    }
});
