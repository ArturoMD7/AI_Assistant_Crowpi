let blobs = [];
let stream;
let rec;
let recordUrl;
let audioResponseHandler;

// Solo grabo el URL a llamar (e.g. /audio) y el 'handler'
// o 'callback' a llamar cuando termine la grabación
function recorder(url, handler) {
    recordUrl = url;
    if (typeof handler !== "undefined") {
        audioResponseHandler = handler;
    }
}

/**
 * Al ser un proyecto pequeño uso doc.getById como maniaco
 * Si no te gusta, puedes cambiarlo ;)
 */
async function record() {
    try {
        document.getElementById("text").innerHTML = "<i>Grabando...</i>";
        document.getElementById("record").style.display = "none";
        document.getElementById("stop").style.display = "";
        document.getElementById("record-stop-label").style.display = "block";
        document.getElementById("record-stop-loading").style.display = "none";
        document.getElementById("stop").disabled = false;

        blobs = [];

        // Grabar audio, blabla
        stream = await navigator.mediaDevices.getUserMedia({ audio: {sampleRate: 44100, channelCount: 1, echoCancellation: true, noiseSuppression: true, autoGainControl: false}, video: false });
        rec = new MediaRecorder(stream);
        rec.ondataavailable = e => {
            if (e.data) {
                blobs.push(e.data);
            }
        };

        rec.onstop = doPreview;

        rec.start();
    } catch (e) {
        alert("No fue posible iniciar el grabador de audio! Favor de verificar que se tenga el permiso adecuado, estar en HTTPS, etc...");
    }
}

function doPreview() {
    if (!blobs.length) {
        console.log("No hay blobios!");
    } else {
        console.log("Tenemos blobios!");
        const blob = new Blob(blobs);

        // Usar fetch para enviar el audio grabado a Pythonio
        var fd = new FormData();
        fd.append("audio", blob, "recording.mp3");

        fetch(recordUrl, {
            method: "POST",
            body: fd,
        })
            .then((response) => response.json())
            .then(audioResponseHandler)
            .catch(err => {
                // Puedes hacer algo más inteligente aquí
                console.log("Oops: Ocurrió un error", err);
            });
    }
}

function stop() {
    document.getElementById("record-stop-label").style.display = "none";
    document.getElementById("record-stop-loading").style.display = "block";
    document.getElementById("stop").disabled = true;

    rec.stop();
}

// Llamar al handler en caso que exista
function handleAudioResponse(response) {
    if (!response || response == null) {
        // TODO subscribe you thief
        console.log("No response");
        return;
    }

    document.getElementById("record").style.display = "";
    document.getElementById("stop").style.display = "none";

    if (audioResponseHandler != null) {
        audioResponseHandler(response);
    }

    // Reproducir el archivo de audio con un timestamp para evitar caché
    if (typeof response.file !== "undefined") {
        let audio = new Audio();
        audio.src = "static/" + response.file + "?t=" + new Date().getTime(); // Evitar caché
        audio.play();
    }

    // Mostrar el código del buzzer si está presente
    if (typeof response.code !== "undefined") {
        document.getElementById("buzzer-code").textContent = response.code;
        Prism.highlightAll(); // Resaltar la sintaxis
    } else {
        document.getElementById("buzzer-code").textContent = ""; // Borrar el código si no es relevante
    }
}
