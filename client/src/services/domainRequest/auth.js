// import { post } from "../requestHelper"

export const login = async (body) => {
    let formData = new FormData();
    formData.append("", "");
    formData.append("username", body.username);
    formData.append("password", body.password);
    try {
        const method = "POST";
        const url = `/api/users/login/token`
        const res = await fetch(url, {
            method,
            body: formData ? formData : undefined,
        });

        const dataObj = await res.clone().json();
        // console.log(dataObj);
        if (!res.ok) {
            alert(`${dataObj.detail}`);
        }
        return res
    } catch (err) {
        console.error(err);
    }

    // return await post('/users/login/token', body);
}