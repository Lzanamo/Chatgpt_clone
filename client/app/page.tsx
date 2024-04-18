"use client";

import React, { useEffect, useState } from "react";
import Sidebar from "./components/Sidebar";
import Chat from "@/app/components/Chat"

async function postData()  {
  await fetch("http://127.0.0.1:8080/api/home", {
    method: "POST",
    headers: {
      "Content-Type": "Access-Control-Allow-Origin",
    },
    body: JSON.stringify("hello"),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    });

}

export default function Home() {
  const [isComponentVisible, setIsComponentVisible] = useState(false);
  //const { trackEvent } = useAnalytics();

  const toggleComponentVisibility = () => {
    setIsComponentVisible(!isComponentVisible);
  };

  

  return (
    <main className="overflow-hidden w-full h-screen relative flex">
      <div className="dark hidden flex-shrink-0 bg-gray-900 md:flex md:w-[260px] md:flex-col">
        <div className="flex h-full min-h-0 flex-col ">
          <Sidebar />
        </div>
      </div>
      <Chat toggleComponentVisibility = { toggleComponentVisibility } />
    </main>
  );
}

