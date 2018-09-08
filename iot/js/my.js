
$(function() {
    var startDate;
    var endDate;
    
    var selectCurrentWeek = function() {
        window.setTimeout(function () {
            $('.week-picker').find('.ui-datepicker-current-day a').addClass('ui-state-active')
        }, 1);
    }
    
    $('.week-picker').datepicker( {
        showOtherMonths: true,
        selectOtherMonths: true,
        onSelect: function(dateText, inst) { 
            var date = $(this).datepicker('getDate');
            startDate = new Date(date.getFullYear(), date.getMonth(), date.getDate() - date.getDay());
            endDate = new Date(date.getFullYear(), date.getMonth(), date.getDate() - date.getDay() + 6);
            startDate1 = new Date(date.getFullYear(), date.getMonth(), date.getDate() - date.getDay() + 1);
            startDate2 = new Date(date.getFullYear(), date.getMonth(), date.getDate() - date.getDay() + 2);
            startDate3 = new Date(date.getFullYear(), date.getMonth(), date.getDate() - date.getDay() + 3);
            startDate4 = new Date(date.getFullYear(), date.getMonth(), date.getDate() - date.getDay() + 4);
            startDate5 = new Date(date.getFullYear(), date.getMonth(), date.getDate() - date.getDay() + 5);         

 var date2 = new Date(startDate1);
    $(".startDate1").datepicker({
        dateFormat: 'yy/mm/dd'
    }).datepicker('setDate', date2);

     var date2 = new Date(startDate2);
    $(".startDate2").datepicker({
        dateFormat: 'yy/mm/dd'
    }).datepicker('setDate', date2);

     var date2 = new Date(startDate3);
    $(".startDate3").datepicker({
        dateFormat: 'yy/mm/dd'
    }).datepicker('setDate', date2);

     var date2 = new Date(startDate4);
    $(".startDate4").datepicker({
        dateFormat: 'yy/mm/dd'
    }).datepicker('setDate', date2);

     var date2 = new Date(startDate5);
    $(".startDate5").datepicker({
        dateFormat: 'yy/mm/dd'
    }).datepicker('setDate', date2);

     var date2 = new Date(endDate);
    $(".endDate").datepicker({
        dateFormat: 'yy/mm/dd'
    }).datepicker('setDate', date2);

//header date
 var date2 = new Date(startDate1);
    $("#startDate1").datepicker({
        dateFormat: 'dd/mm/yy'
    }).datepicker('setDate', date2);

     var date2 = new Date(startDate2);
    $("#startDate2").datepicker({
          dateFormat: 'dd/mm/yy'
    }).datepicker('setDate', date2);

     var date2 = new Date(startDate3);
    $("#startDate3").datepicker({
          dateFormat: 'dd/mm/yy'
    }).datepicker('setDate', date2);

     var date2 = new Date(startDate4);
    $("#startDate4").datepicker({
          dateFormat: 'dd/mm/yy'
    }).datepicker('setDate', date2);

     var date2 = new Date(startDate5);
    $("#startDate5").datepicker({
         dateFormat: 'dd/mm/yy'
    }).datepicker('setDate', date2);

     var date2 = new Date(endDate);
    $("#endDate").datepicker({
          dateFormat: 'dd/mm/yy'
    }).datepicker('setDate', date2);

    jQuery('#ttable').css('opacity', '1');
    jQuery('#ttable').css('visibility', 'visible');

            selectCurrentWeek();
        },
        beforeShowDay: function(date) {
            var cssClass = '';
            if(date >= startDate && date <= endDate)
                cssClass = 'ui-datepicker-current-day';
            return [true, cssClass];
        },
        onChangeMonthYear: function(year, month, inst) {
            selectCurrentWeek();
        }
    });
    
    $('.week-picker .ui-datepicker-calendar tr').live('mousemove', function() { $(this).find('td a').addClass('ui-state-hover'); });
    $('.week-picker .ui-datepicker-calendar tr').live('mouseleave', function() { $(this).find('td a').removeClass('ui-state-hover'); });
});