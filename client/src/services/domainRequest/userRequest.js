import {get, post} from "../requestHelper";
const entity = 'users';

export const createUser = async (body) => {
    return await post(`${entity}/`, body);
}
export const getUser = async (id,  token) => {
    return await get(entity, id, token);
}