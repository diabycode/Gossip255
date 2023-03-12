/* Module for get post liked status */

/**
 * Update vote in database and return new vote count
 * @param {String} postId 
 * @param {String} csrftoken 
 */
async function updateVoteInDB (postId, csrftoken) {
    const response = await fetch("/reactions/update_vote/", {
        method: 'POST',
        headers: {
            "Accept": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({
            post_id: postId,
        }),
    })
    
    if (response.ok) {
        return response.json()
    }

}

/**
 * Update a post vote status
 * @param {*} post 
 * @param {String} newVoteCount
 * @param {Boolean} CurrentUserHasVote
 */
function UpdateVoteStatus (post, newVoteCount, currentUserHasVote) {
    post.querySelector(".stats .vote-count").innerText = newVoteCount
    if (currentUserHasVote) {
        post.querySelector("form button > svg").style.fill = "#53687E"
    } else {
        post.querySelector("form button > svg").style.fill = ""
    }
}


/**
 * Get post element from button element
 * @param {HTMLElement} btn
 */
function getPostElement(btn){
    return btn.closest(".post")
}


// Update vote status when user vote
document.querySelectorAll(".post form button").forEach(btn => {
    btn.addEventListener("click", (event) => {
        event.preventDefault()

        const post = getPostElement(event.target)
        const csrftoken = post.querySelector("input[name='csrfmiddlewaretoken']").value
        updateVoteInDB(post.getAttribute("id"), csrftoken)
            .then(data => {
                UpdateVoteStatus(post, data.vote_count, data.current_user_has_vote)
            })
    
    })
})


/**
 * get post vote status from database
 * @param {String} postId
 */
async function getPostStatus (postId) {
    const response = await fetch(`/post/vote_status/${postId}/`, {
        method: 'GET',
        headers: {
            "Accept": "application/json",
        }
    });

    if (response.ok) {
        return response.json();
    }
}



/** 
 * Update many posts vote status
*/
function UpdateVotesStatus (posts) {
    posts.forEach(post => {
        getPostStatus(post.getAttribute("id"))
            .then(data => {
                UpdateVoteStatus(post, data.vote_count, data.has_vote)
            })
    })
}


// Update vote status when page load
window.addEventListener("load", () => {
    const all_post = document.querySelectorAll(".post")
    UpdateVotesStatus(all_post)
});



