Spotter: Your Ultimate AI-Driven Fitness Companion
Spotter is a comprehensive full-stack fitness application designed to simplify health tracking and workout management. Built with a focus on precision and user experience, it serves as a digital personal trainer that helps users monitor their nutritional intake, manage weight goals, and access structured workout guidance.

## Core Features
Dynamic Calorie & Macro Calculator: Precision tools to calculate Daily Energy Expenditure (TDEE) and macronutrient requirements based on individual body metrics.

Targeted Transformation Plans: Specialized logic for weight loss, maintenance, and muscle gain, providing users with tailored caloric targets.

Workout Routine Guidance: A structured database of exercises and routines designed to ensure proper form and consistent progress.

Progress Tracking: Integrated health monitoring to log weight changes and workout consistency over time.

Interactive Dashboard: A sleek, user-centric interface for a birds-eye view of daily fitness goals and achievements.

## Technical Stack
The architecture of Spotter focuses on scalability, security, and a high-performance database structure.

Backend: Django (Python) – Leveraged for its robust ORM and secure authentication systems.

Frontend: HTML5, CSS3, and JavaScript – Featuring a custom "Rubbish Red" and Black aesthetic with gritty, bold typography for a high-intensity gym atmosphere.

Database: PostgreSQL – Utilized for complex data relationships between users, workouts, and nutritional logs.

Version Control: Managed via Git and hosted on GitHub.

## Project Architecture & Logic
The application follows a Model-View-Template (MVT) architecture. Key logic components include:

The Calculation Engine: Uses standardized fitness formulas (like Mifflin-St Jeor) within Django views to process user data and return real-time health insights.

Relational Data Mapping: A PostgreSQL schema that connects exercises to specific muscle groups and user-specific workout logs.

Frontend Styling: Custom CSS variables define the signature "dark mode" theme, ensuring a consistent brand identity across all modules.
