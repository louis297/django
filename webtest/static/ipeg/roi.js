/**
 * Created by louis on 4/7/16.
 */
const reducesSiteVisitsBy = .15;
const reducesCableCutsBy = .02;
const reducesTrainingTimeBy = .25;
const reducesTimeToFindABuriedFacility = .30;

$(document).ready(function(){
    $("#input1").change(function(){
        $("#testspan").val($("#input1").val())
    })
}