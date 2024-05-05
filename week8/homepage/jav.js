document.addEventListener('DOMContentLoaded', function()
    {
        document.querySelector('form').addEventListener('submit', function(e)
        {
            alert('Hello Wanderer named, ' + document.querySelector('#name').value  + "!! \nContinue Below for an adventure");
            e.preventDefault();
            });

            let right =  document.querySelector('.right');
                right.addEventListener('click', function()
                {
                    right.style.backgroundColor = 'green';
                    document.querySelector('#response').innerHTML = 'Here is a Cookie';
                });

            let wrongs = document.querySelectorAll('.wrong');
                for (let i = 0; i < wrongs.length; i++)
                {
                    wrongs[i].addEventListener('click', function()
                    {
                        wrongs[i].style.backgroundColor = 'red';
                        document.querySelector('#response').innerHTML = 'No Cookie for you this time!';
                    });
                }
                document.querySelector('#test').addEventListener('click',function()
                {
                    let input = document.getElementById("i2");
                    if (input.value == 'Privet Drive')
                    {
                        document.getElementById("i2").style.backgroundColor = "green";
                        document.querySelector('#r2').innerHTML = 'Here is a Cookie';
                    }
                    else
                    {
                        document.getElementById("i2").style.backgroundColor = "red";
                        document.q1uerySelector("#r2").innerHTML = 'No Cookie for you this time!';
                    }
                });
            });
