# Nyereka
# Social Media Data Deletion App

## Overview
This application allows users to delete their personal data from social media platforms such as Facebook and Instagram. It integrates with external APIs to facilitate data removal while ensuring security and privacy.

## Features
- **Login with Facebook & Instagram**
- **Fetch user data** before deletion
- **Securely delete user data** from linked accounts
- **Modern UI** inspired by Jarvis and ShotDeck
- **Responsive design** with smooth animations

## Technologies Used
- **Frontend:** HTML, CSS (Glassmorphism & Neon UI), JavaScript
- **Backend:** Python (Flask API)
- **External APIs:** Facebook & Instagram Graph API
- **Deployment:** Web servers with Load Balancer (Web01, Web02, Lb01)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/social-media-data-deletion-app.git
   cd social-media-data-deletion-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt  # For backend
   npm install  # For frontend
   ```
3. Set up environment variables in `.env`:
   ```
   FB_CLIENT_ID=your_facebook_client_id
   FB_CLIENT_SECRET=your_facebook_client_secret
   INSTAGRAM_CLIENT_ID=your_instagram_client_id
   INSTAGRAM_CLIENT_SECRET=your_instagram_client_secret
   BACKEND_URL=http://localhost:5000
   ```
4. Start the backend:
   ```bash
   python app.py
   ```
5. Start the frontend:
   ```bash
   npm start
   ```
6. Deploy the app on web servers and configure load balancer.

## Deployment Notes
- Ensure API keys are stored securely.
- Verify CORS settings to allow frontend-backend communication.
- Test the load balancer to confirm traffic distribution.

## License
This project is open-source under the MIT License together with chatgpt.

