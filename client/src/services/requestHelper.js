const apiUrl = '/api';

export const get = async (entityName, id = '', token = '') => {
    return await makeRequest(`${entityName}/${id}`, 'GET', null, token);
}

export const post = async (entityName, body) => {
    return await makeRequest(entityName, 'POST', body);
}

export const put = async (entityName, id, body) => {
    return await makeRequest(`${entityName}/${id}`, 'PUT', body);
}

export const deleteReq = async (entityName, id) => {
    return await makeRequest(`${entityName}/${id}`, 'DELETE');
}

const makeRequest = async (path, method, body, token = '') => {
    try {
        const url = `${apiUrl}/${path}`
        const res = await fetch(url, {
            method,
            body: body ? JSON.stringify(body) : undefined,
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            }
        });

        const dataObj = await res.clone().json();


        if (!res.ok) {
            alert(`${dataObj.detail}`);
        }

        // return dataObj;
        return res
    } catch (err) {
        console.error(err);
    }
}