const image_input = document.querySelector("#imageUpload");
let predict_btn = document.querySelector("#btn-predict")
var uploaded_image = "";

function readURL(input){
	if (input.files && input.files[0]){
		var reader = new FileReader()
		reader.addEventListener("load", ()=>{
			uploaded_image = reader.result;
			document.querySelector("#imagePreview").style.backgroundImage = `url(${uploaded_image})`
		})
		reader.readAsDataURL(input.files[0])
	}
}

image_input.addEventListener("change", function(){
	document.querySelector(".image-section").style.display = "block"
    document.querySelector("#btn-predict").style.display = "block"
    document.querySelector("#result").text = ""
    document.querySelector("#result").style.display = "none"
	readURL(this)
})
predict_btn.addEventListener("click",function(){
	var form_data = new FormData(document.querySelector("#upload-file"));
    predict_btn.style.display = "none"
    document.querySelector(".loader").style.display = "block"
    const otherParam = {
    	body: form_data,
    	method: "POST"
    }
    fetch("/predict",otherParam).then(data=>{
    	return data.text()
    }).then(res=>{
    	document.querySelector("#result").innerHTML = res
        document.querySelector("#result").style.display = "block"
        document.querySelector(".loader").style.display = "none"
    }).catch(error=>console.log(error))
})














