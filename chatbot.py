career_data = {
    "data scientist": {
    "description": "A Data Scientist analyzes data and builds intelligent models to solve real-world problems.",

    "skills": [
        "Python",
        "Statistics",
        "Pandas",
        "NumPy",
        "Machine Learning"
    ],

    "roadmap": [
        "Learn Python",
        "Learn Data Analysis",
        "Learn Machine Learning",
        "Build Projects",
        "Create Portfolio"
    ],

    "resources": [
        "Kaggle",
        "Coursera",
        "YouTube"
    ],

    "careers": [
        "Data Scientist",
        "ML Engineer",
        "AI Engineer"
    ]
},
    "data analyst": {
    "description": "A Data Analyst collects, processes and analyzes data to help organizations make decisions.",

    "skills": [
        "Excel",
        "SQL",
        "Python",
        "Power BI",
        "Data Visualization"
    ],

    "roadmap": [
        "Learn Excel",
        "Learn SQL",
        "Learn Python",
        "Learn Power BI",
        "Build Data Projects"
    ],

    "resources": [
        "Coursera",
        "Kaggle",
        "YouTube"
    ],

    "careers": [
        "Data Analyst",
        "Business Analyst",
        "BI Analyst"
    ]
},
    "ai engineer": {
    "description": "An AI Engineer develops intelligent systems using machine learning and artificial intelligence.",

    "skills": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch"
    ],

    "roadmap": [
        "Learn Python",
        "Learn ML",
        "Learn Deep Learning",
        "Build AI Projects",
        "Create Portfolio"
    ],

    "resources": [
        "Coursera",
        "DeepLearning.AI",
        "YouTube"
    ],

    "careers": [
        "AI Engineer",
        "ML Engineer",
        "Research Engineer"
    ]
},
    "software engineer": {
    "description": "A Software Engineer designs and develops software applications.",

    "skills": [
        "Programming",
        "Data Structures",
        "Algorithms",
        "Databases",
        "Git"
    ],

    "roadmap": [
        "Learn Programming",
        "Learn DSA",
        "Learn Databases",
        "Build Projects",
        "Practice Interviews"
    ],

    "resources": [
        "LeetCode",
        "GeeksforGeeks",
        "YouTube"
    ],

    "careers": [
        "Software Engineer",
        "Backend Developer",
        "System Engineer"
    ]
},
    "web developer": {
    "description": "A Web Developer builds websites and web applications.",

    "skills": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js"
    ],

    "roadmap": [
        "Learn HTML",
        "Learn CSS",
        "Learn JavaScript",
        "Learn React",
        "Build Projects"
    ],

    "resources": [
        "MDN",
        "freeCodeCamp",
        "YouTube"
    ],

    "careers": [
        "Frontend Developer",
        "Backend Developer",
        "Full Stack Developer"
    ]
},
    "flutter developer": {
    "description": "A Flutter Developer builds cross-platform mobile applications.",

    "skills": [
        "Dart",
        "Flutter",
        "Firebase",
        "REST APIs",
        "State Management"
    ],

    "roadmap": [
        "Learn Dart",
        "Learn Flutter",
        "Learn Firebase",
        "Build Apps",
        "Publish Projects"
    ],

    "resources": [
        "Flutter Docs",
        "YouTube",
        "Udemy"
    ],

    "careers": [
        "Flutter Developer",
        "Mobile App Developer",
        "Software Engineer"
    ]
}
}
responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I am fine.",
    "what is your name": "I am a Rule-Based AI Chatbot.",
    "bye": "Goodbye!",
    "thanks": "You're welcome!",
    "good morning": "Good Morning!",
    "good evening": "Good Evening!",
    "help": "I can answer simple questions.",
    "python": "Python is a programming language.",
    "ai": "AI stands for Artificial Intelligence.",
    "who made you": "I was created by Javeria.",
    "what can you do": "I can answer predefined questions.",
    "welcome": "Thank you!",
    "good night": "Good Night!",
    "computer": "A computer is an electronic device.",
    "coding": "Coding is the process of writing programs.",
    "programming": "Programming is creating software.",
    "student": "Students learn new skills every day.",
    "university": "A university provides higher education."
}

print("=" * 60)
print("🤖 CareerBot - AI Career Guidance Assistant")
print("=" * 60)
print("Type 'help' to see commands")
print("Type 'topics' to see available careers")
print("Type 'exit' to quit")
print("=" * 60)

while True:
    user_input = input("\nYou: ")

    clean_input = user_input.lower().strip()

    if clean_input == "exit":
        print("Chatbot: Goodbye! Have a nice day!")
        break

    if clean_input == "help":
        print("\n========== HELP MENU ==========")
        print("General Commands:")
        print("- hello / hi     : Start conversation")
        print("- help           : Show help menu")
        print("- topics         : Show all career topics")
        print("- exit           : Close CareerBot")
        
        print("\nCurrent Career Topics:")
        print("- Data Scientist")
        print("- Data Analyst")
        print("- AI Engineer")
        print("- Software Engineer")
        print("- Web Developer")
        print("- Flutter Developer")
        print("\nUse a career name to get guidance.")
        print("Example: data scientist")

        continue

    if clean_input == "topics":
        print("\n========== AVAILABLE TOPICS ==========")

        for topic in career_data:
            print("-", topic.title())

        continue

    if clean_input in career_data:

        career = career_data[clean_input]

        print("\n==============================")
        print("Career:", clean_input.title())
        print("==============================")

        print("\nDescription:")
        print(career["description"])

        print("\nRequired Skills:")
        for skill in career["skills"]:
            print("-", skill)

        print("\nRoadmap:")
        for step in career["roadmap"]:
            print("-", step)

        print("\nResources:")
        for resource in career["resources"]:
            print("-", resource)

        print("\nCareer Opportunities:")
        for job in career["careers"]:
            print("-", job)

        continue

    reply = responses.get(
        clean_input,
        "Sorry, I do not understand. Please try another question."
    )

    print("Chatbot:", reply)