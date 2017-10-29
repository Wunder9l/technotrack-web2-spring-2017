export function getCsrfToken() {
    return document.cookie.match(/csrftoken=([^ ;]+)/)[1];
}
