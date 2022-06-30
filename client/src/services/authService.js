import {getObjectFromLocalStorage, setLocalStorageItem} from "./localStorageHelper";

export const isSignedIn = () => {
    const user = getObjectFromLocalStorage('user');
    return user ? true : false;
};
export const getCurrentUser = () => {
    return getObjectFromLocalStorage('user');
}

export const setLoginSession = (user) => {
    setLocalStorageItem('user', user);
}

export const unsetLoginSession = () => {
    setLocalStorageItem('user', null);
}