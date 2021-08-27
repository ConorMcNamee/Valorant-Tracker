import React,{ useEffect, useState }  from "react";
import axios from "axios";

const API = () => {

    
    const fetchUserData = async () => {
        const valoratnRes = await fetch("http://127.0.0.1:5000/acc-data")
        // const AccountData = await accountRes.json()
        const valData = await valoratnRes.json()
        console.log(valData)
    }

    useEffect(() => {
        fetchUserData()
    }, []);

    return(
        <div>
        </div>
    )
}

export default API;