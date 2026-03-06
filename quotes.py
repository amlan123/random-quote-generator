import random

quotes = [
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "Be yourself; everyone else is already taken.", "author": "Oscar Wilde"},
    {"text": "In the middle of difficulty lies opportunity.", "author": "Albert Einstein"},
    {"text": "Stay hungry, stay foolish.", "author": "Steve Jobs"},
    {"text": "The unexamined life is not worth living.", "author": "Socrates"},
    {"text": "Why do we fall? So we can learn to pick ourselves up.", "author": "Batman"},
]

random_quote = random.choice(quotes)
print(f'"{random_quote["text"]}"')
print(f'  — {random_quote["author"]}')
```

Run it again. Now your output should look like:
```
"Stay hungry, stay foolish."
  — Steve Jobs
