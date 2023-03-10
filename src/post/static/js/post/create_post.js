export const imgContainer = document.querySelector("#image-selected-container")
const imgInput = document.querySelector("form input[type=file]") 

if (imgInput.files[0]) {
    console.log("ok")
}

export function clearPreview () {
    imgContainer.innerHTML = ""
    imgContainer.style.display = ""
    document.querySelector(".image-input").style.display = ""

    imgInput.value = ""
}


export function showImagePreview () {
    var reader = new FileReader()
    reader.readAsDataURL(imgInput.files[0])

    reader.onload = function () {
        const img = document.createElement("img")
        img.setAttribute("src", reader.result)

        imgContainer.style.display = "block"

        // add image
        imgContainer.innerHTML = ""
        imgContainer.appendChild(img)

        // clear button 
        const btn = document.createElement("span")
        btn.innerText = "supprimer"
        imgContainer.appendChild(btn)
        btn.addEventListener("click", () => {
            clearPreview()
        })
    }
}



imgInput.addEventListener("change", () => {
    document.querySelector(".image-input").style.display = "none"
    showImagePreview()
})