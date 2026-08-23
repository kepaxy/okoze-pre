const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

let mouseX = 0;
let mouseY = 0;

canvas.addEventListener("mousemove", (event) => {
    const rect = canvas.getBoundingClientRect();

    mouseX = event.clientX - rect.left;
    mouseY = event.clientY - rect.top;

    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 3, 0, Math.PI * 2);
    ctx.fill();
});

document.addEventListener("paste", (event) => {
    const items = event.clipboardData.items;

    for (const item of items) {
        if (!item.type.startsWith("image/")) {
            continue;
        }

        const file = item.getAsFile();

        if (!file) {
            continue;
        }

        const image = new Image();

        image.onload = () => {
            ctx.drawImage(image, mouseX, mouseY);
            URL.revokeObjectURL(image.src);
        };

        image.src = URL.createObjectURL(file);
    }
});