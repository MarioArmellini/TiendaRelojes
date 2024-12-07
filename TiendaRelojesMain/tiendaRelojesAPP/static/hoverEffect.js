$(document).ready(function() {
    // Efecto de opacidad en las imágenes
    $('.reloj img').hover(
        function() {
            $(this).css('opacity', '0.9');
        },
        function() {
            $(this).css('opacity', '1');
        }
    );

    // Tooltip con detalles del reloj usando AJAX
    $('.reloj').hover(
        function(event) {
            const relojId = $(this).data('id');  // Asegúrate de que `data-id` esté bien configurado
            if (!relojId) {
                console.error('No se encontró el ID del reloj.');
                return;  // Si no se encuentra el ID, no continuar
            }

            const tooltip = $('#tooltip');
            console.log(`Se ha hecho hover sobre el reloj con ID: ${relojId}`);

            // Solicitar detalles por AJAX
            $.ajax({
                url: `/reloj/${relojId}/detalle_ajax/`,
                method: 'GET',
                success: function(data) {
                    console.log('Datos obtenidos:', data);
                    tooltip.html(`
                        <strong>${data.nombre} (${data.marca})</strong>
                        <p>${data.precio}</p>
                    `);
                    tooltip.css({
                        display: 'block',
                        top: event.pageY + 10,
                        left: event.pageX + 10
                    });
                },
                error: function(xhr, status, error) {
                    console.error('Error AJAX:', status, error);
                    tooltip.text('Error al cargar detalles').css('display', 'block');
                }
            });
        },
        function() {
            console.log('Mouse out del reloj');
            $('#tooltip').hide();
        }
    );

    // Mover el tooltip con el ratón
    $('.reloj').mousemove(function(event) {
        $('#tooltip').css({
            top: event.pageY + 10,
            left: event.pageX + 10
        });
    });
});
