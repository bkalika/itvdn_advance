let closeBtn = document.querySelector(".btn-close");

moreDetailButtons.forEach(function(btn){
    btn.addEventListener("click", openModal)
})

function openModal(){
    modal.classList.add("show")
    modal.classList.remove("hide")
}

function closeModal(){
    modal.classList.add("hide");
    modal.classList.remove("show")
}

function openModalByScroll(){
    // show current scroll stage
    let scrollSize = window.pageYOffset
    // show full page size
    let fullPageSize = document.documentElement.ScrollHeight
    if (scrollSize >= fullPageSize / 2){
        openModal();
        window.removeEventListener('scroll', openModalByScroll);
    }
}

window.addEventListener("scroll", openModalByScroll);

closeBtn.addEventListener("click", closeModal);

modal.addEventListener("click", function(e){
    if(e.target === modal){
        closeModal()
    }
})
