import React, { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import queryString from "query-string";
import axios from "axios";
import "./index.css";
const { BACKEND_API_URL } = process.env;

// const  BACKEND_API_URL = "http://192.168.2.21:8000"


const SocialAuth = () => {
  let location = useLocation();
  console.log("location", location);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const values = queryString.parse(location.search);
    const code = values.code ? values.code : null;
      
    if (code) {
      onGogglelogin();
    }
  }, [location.search]);
  const googleLoginHandler = (code) => {
    console.log("Sending request to backend with code:", code); // Add this line
    return axios
      // .get(`${BACKEND_API_URL}/api/auth/login/google/${code}`)
      .get(`${BACKEND_API_URL}/api/v1/auth/google-login/${code}`)
      .then((res) => {
        console.log("Response from backend:", res); // Add this line
        localStorage.setItem("googleFirstName", res.data.response.user.username);
        localStorage.setItem("access_token", res.data.response.access_token);

        navigate('/success');
        return res.data;
      })
      .catch((err) => {
        console.log("Error from backend:", err); // Add this line
        return err;
      });
  };
  
  const onGogglelogin = async () => {
    const response = await googleLoginHandler(location.search);
    console.log("Google login response:", response); // Add this line
    if (response.data && response.data.access) {
      console.log("Access token received:", response.data.access); // Add this line
      navigate("/");
    }
  }

  return (
    <div className="loading-icon-container">
      <div className="loading-icon">
        <div className="loading-icon__circle loading-icon__circle--first"></div>
        <div className="loading-icon__circle loading-icon__circle--second"></div>
        <div className="loading-icon__circle loading-icon__circle--third"></div>
        <div className="loading-icon__circle loading-icon__circle--fourth"></div>
      </div>
        <small className=" text-center mr-2">
          Just a moment
        </small>
    </div>
  );
};


export default SocialAuth;
