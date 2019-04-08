$(document).ready( function() {
    $("#id_bairro").change( function(event) {
        var bairro = $(this).val();
        
        $.ajax({
            url: '/ajax/escolha_bairro/',
            data: {
                'bairro': bairro
            },
            success: function (data) {
                ruas = data.nomes.split(","); 
                ruas.sort();
                str = '';                
                for( i=1; i<ruas.length; i++ ){
                    str += '<option value="' + ruas[i] + '">' + ruas[i].toUpperCase() + '</option>';
                }
                $("#id_nome").html(str);
            },
            dataType: 'json'
        });

    });
});

