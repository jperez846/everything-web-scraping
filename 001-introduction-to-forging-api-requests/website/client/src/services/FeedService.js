const isCodespaces = process.env.REACT_APP_CODESPACE_NAME != "" && process.env.REACT_APP_GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN != "";

let BACKEND_URL = isCodespaces
    ? `https://${process.env.REACT_APP_CODESPACE_NAME}-${process.env.REACT_APP_BACKEND_PORT}.${process.env.REACT_APP_GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}`
    : `http://${process.env.REACT_APP_BACKEND_HOST}:${process.env.REACT_APP_BACKEND_PORT}`;
//    BACKEND_URL=`http://localhost:8080`
//let envVars = `http:${process.env.REACT_APP_BACKEND_HOST}:${process.env.REACT_APP_BACKEND_PORT}`;
//console.log("ENV VARS");
//console.log(envVars);

console.log("BACKEND URL update02:");
console.log(BACKEND_URL);

export async function getFeed(page) {
console.log("TRYING TO FETCH FEED")
    try{
        const response = await fetch(`${BACKEND_URL}/feed/${page}`); 
        return response.json();
    }catch(error) {
        return new Promise((res, rej) => {
            res([])
        });
    }
    
}


export async function getProfileFeed(username, page) {
    try{
        const response = await fetch(`${BACKEND_URL}/profile/${username}/feed/${page}`); 
        return response.json();
    }catch(error) {
        return new Promise((res, rej) => {
            res([])
        });
    }
    
}