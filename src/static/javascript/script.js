// SEARCH JS
document.getElementById(id_q).value = "{{ query }}"


//CONTACT US AJAX FORM
$(document).ready(function(){
    var $myForm = $('.my-ajax-form1');
    $myForm.submit(function(event){
        event.preventDefault()
        var $formData = $myForm.serialize();
        var $thisURL = $myForm.attr('data-url')
        $.ajax({
                method:'POST',
                url: $thisURL,
                data: $formData,
                success : handleSuccess,
                error: handleError,
        });
        function handleSuccess(data){
            console.log(data.message)
            t= data.message
            $('#response').html(t)
            $('#response').addClass('alert alert-success')
            $myForm[0].reset()
        }
        function handleError(ThrowError){
            console.log(ThrowError)
        }
    });
});