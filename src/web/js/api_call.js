const userAction = () => {
    console.log("Hello")
    form_data = document.querySelector(".data-input")
    console.log(form_data)
    data = form_data.value
    console.log(data)
    request_body = {
        "data": body
    }
    const response = await fetch('http://127.0.0.1:8000/api/result/', {
        method: 'POST',
        body: json.parse(request_body),
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const myJson = await response.json();
    console.log(myJson)
}