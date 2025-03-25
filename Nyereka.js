import React, { useState } from "react";
import axios from "axios";

const backendURL = process.env.REACT_APP_BACKEND_URL; // Load backend URL from .env

function App() {
    const [userData, setUserData] = useState(null);

    const login = (platform) => {
        window.location.href = `${backendURL}/login/${platform}`;
    };

    const fetchData = async () => {
        try {
            const response = await axios.get(`${backendURL}/fetch-data`);
            setUserData(response.data);
        } catch (error) {
            console.error("Error fetching data", error);
        }
    };

    const deleteData = async (platform) => {
        try {
            const response = await axios.delete(`${backendURL}/delete-data/${platform}`);
            alert(response.data.message || response.data.error);
        } catch (error) {
            console.error("Error deleting data", error);
        }
    };

    return (
        <div style={{ textAlign: "center", marginTop: "50px" }}>
            <h1>Social Media Data Deletion App</h1>

            <button onClick={() => login("facebook")}>Login with Facebook</button>
            <button onClick={() => login("instagram")}>Login with Instagram</button>

            <button onClick={fetchData}>Fetch Data</button>

            <button onClick={() => deleteData("facebook")}>Delete Facebook Data</button>
            <button onClick={() => deleteData("instagram")}>Delete Instagram Data</button>

            {userData && (
                <div>
                    <h2>User Info</h2>
                    <p><strong>ID:</strong> {userData.id}</p>
                    <p><strong>Name:</strong> {userData.name}</p>
                    <p><strong>Email:</strong> {userData.email}</p>
                </div>
            )}
        </div>
    );
}

export default App;
