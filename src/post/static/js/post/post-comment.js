
/**
 * @param {String} comment_content 
 * @param {String} postId
 */
async function postComment(comment_content, postId) {
    const csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value

    const response = await fetch("/reactions/comment/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({
            post_id: postId,
            content: comment_content,
        })
    })
    if (response.ok) {
        return response.json()
    }
}


/**
 * @param {Object} commentData
 */
function addCommentToDOM(commentData) {
    const commentStructure = document.querySelector("#comment-template").content.cloneNode(true)

    commentStructure.querySelector("p").innerText = commentData.content
    commentStructure.querySelector("div > p a").innerText = commentData.author
    const authorUrl =  `/account/${commentData.author}/`
    commentStructure.querySelector("div > p a").setAttribute("href", authorUrl)
    commentStructure.querySelector("div > p span").innerText = commentData.created_at
    const commentDeleteUrl = `/reactions/comment/${commentData.pk}/delete/`
    commentStructure.querySelector("div > a").setAttribute("href", commentDeleteUrl)
    commentStructure.querySelector("div > a").innerText = "Supprimer"

    // add comment to conatiner
    const container = document.createElement("div")
    container.classList.add("comment")
    container.appendChild(commentStructure)

    // add comment to DOM
    document.querySelector(".comments-list").prepend(container)
}

console.log("ok")

// post a comment
document.querySelector("#post-comment-btn").addEventListener("click", (event) => {
    event.preventDefault()
    const postId = window.location.href.split("/").slice(-2)[0]

    const commentInput = document.querySelector("form #id_content")
    if (commentInput.value == "") {
        return
    }

    postComment(commentInput.value, postId)
        .then(commentData => {
            addCommentToDOM(commentData)
        })
        .then(() => {
            commentInput.value = ""
        })

})
