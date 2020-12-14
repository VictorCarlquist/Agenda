function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

$(document).on('submit', 'form.form-update', function(e) {
    e.preventDefault();

    var form = $(e.target)[0];
    var url = $(form).attr('action');
    var data = $(form).serializeArray().reduce(function(obj, item) {
        obj[item.name] = item.value;
        return obj;
    }, {});;
    data = JSON.stringify(data);
    console.log(data);
    $.ajax({
        type: "PUT",
        url: url,
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        data: data,
        success: function(data)
        {
            $('.toast').toast('show');
        }
    });
});

$(document).on('submit', 'form.form-add', function(e) {
    e.preventDefault();

    var form = $(e.target)[0];
    var url = $(form).attr('action');
    var data = $(form).serializeArray().reduce(function(obj, item) {
        obj[item.name] = item.value;
        return obj;
    }, {});;
    data = JSON.stringify(data);
    console.log(data);
    $.ajax({
        type: "POST",
        url: url,
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        data: data,
        success: function(data)
        {
            location.reload();
        }
    });
});


function delete_item(url) 
{
    $.ajax({
        type: "DELETE",
        url: url,
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        success: function(data)
        {
            location.reload();
        }
    });
}

function delete_contact(url) 
{
    $.ajax({
        type: "DELETE",
        url: url,
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        success: function(data)
        {
            location.reload();
        }
    });
}