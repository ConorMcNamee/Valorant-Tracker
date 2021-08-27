import React,{ useEffect, useState }  from "react";
import axios from "axios";

const API = () => {

    
    const fetchUserData = async () => {
        const valoratnRes = await fetch("https://ap.api.riotgames.com/val/content/v1/contents?api_key=RGAPI-e056a228-a10e-481c-8338-9469355fc27c")
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