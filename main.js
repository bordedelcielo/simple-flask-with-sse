const source = new EventSource('/stream');

source.addEventListener('greeting', (event) => {
    const data = JSON.parse(event.data);
    const progress = data.progress;
})