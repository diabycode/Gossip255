import { imgContainer, clearPreview } from "./create_post.js";


/**
 * @param {String} imgUrl 
 */
function showImageAssociate (imgUrl) {
    const imgTag = document.createElement("img")
    imgTag.src = imgUrl

    imgContainer.appendChild(imgTag)
    imgContainer.style.display = "block"

    // clear button 
    const btn = document.createElement("span")
    btn.innerText = "supprimer"
    imgContainer.appendChild(btn)
    btn.addEventListener("click", () => {
        clearCheckBox.checked = true
        clearPreview()
    })

}

// get image associated with the post
const img = document.querySelector(".image-input a")
if (img) {
    const imgUrl = img.getAttribute("href")
    showImageAssociate(imgUrl)
    document.querySelector(".image-input").style.display = "none"

}

const imgInput = document.querySelector(".image-input").querySelector("input[type=file]")
const imgInputLabel = document.querySelector(".image-input").querySelector("label[for=id_thumbnail]")
const clearCheckBox = document.querySelector("#thumbnail-clear_id")

document.querySelector(".image-input").innerHTML = ""
document.querySelector(".image-input").appendChild(imgInputLabel)
document.querySelector(".image-input").appendChild(imgInput)
document.querySelector(".image-input").appendChild(clearCheckBox)


