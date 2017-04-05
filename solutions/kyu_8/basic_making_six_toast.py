"""BASIC: Making Six Toast.
https://www.codewars.com/kata/basic-making-six-toast

<h1 id="title">Making Six Toast:</h1>

<div class="part">
<h2 id="heading">STORY:</h2>

<h4 id="text">You are going to make toast fast, you think that you should make multiple pieces of toasts and once. So, you try to make 6 pieces of toast.</h4>

<h2 id="heading">PROBLEM:</h2>

<h4 id="text">You forgot to count the number of toast you put into there, you don't know if you put exactly six pieces of toast into the toasters.</h4>

<h2 id="heading">WHAT TO DO:</h2>

<h4 id="text">Make a function that counts how many more (or less) pieces of toast you need in the toasters. Even though you need more or less, the number will still be positive, not negative.</h4>

<h2 id="heading">EXAMPLE:</h2>

<h4 id="text">You must return the number of toast the you need to put in (or to take out). Let's say you put five in:</h4>

<h4 id="subheading">JAVASCRIPT:</h4>

```
  // The "5" is how many pieces you put in.
```
```
  sixToast(5);
```
```
  // It should return 1.
```
```
  function sixToast(num) {
```
```
    // code
```
```
    return 1;
```
```
  }
```

<h4 id="subheading">COFFEESCRIPT:</h4>

```
  # The "5" is how many pieces you put in.
```
```
  sixToast(5)
```
```
  # It should return 1.
```
```
  sixToast=(num) ->
```
```
    # code
```
```
    return 1
```
  
<h4 id="subheading">PYTHON:</h4>
  
```
  # The "5" is how many pieces you put in:
  sixToast(5)
```
```
  # It should return 1.
```
```
  def six_toast(num):
```
```
  # code
```
```
    return 1
```
  
<h4 id="subheading">RUBY:</h4>
  
```
  # The "5" is how many pieces you put in.
```
```
  six_toast(5)
```
```
  # It should return 1.
```
```
  def six_toast(num)
```
```
    # code
```
```
    return 1
```
```
  end
```

<h4 id="text">This time you put twelve in:</h4>

<h4 id="subheading">JAVASCRIPT:</h4>
  
```
  // The "12" is how many pieces you put in.
```
```
  sixToast(12);
```
```
  // It should return 6, not -6.
```
```
  function sixToast(num) {
```
```
    // code
```
```
    return 6;
```
```
  }
```
  
<h4 id="subheading">COFFEESCRIPT:</h4>
  
```
  # The "12" is how many pieces you put in.
```
```
  sixToast(12)
```
```
  # It should return 6, not -6.
```
```
  sixToast=(num) ->
```
```
    # code
```
```
    return 6
```
  
<h4 id="subheading">PYTHON:</h4>
  
```
  # The "12" is how many pieces you put in.
```
```
  sixToast(12)
```
```
  # It should return 6, not -6.
```
```
  def six_toast(num):
```
```
  # code
```
```
  return 6
```
  
<h4 id="subheading">RUBY:</h4>
  
```
  # The "12" is how many pieces you put in.
```
```
  six_toast(12)
```
```
  # It should return 6, not -6.
```
```
  def six_toast(num)
```
```
    # code
```
```
    return 6
```
```
  end
```

<h2 id="text">Good luck!</h2>
</div>

<style>
#title, #text, #heading {
  text-align:center;
}
.part {
  background-color:#000033;
  padding:3%;
}
#title {
  background-color:#0022FF;
  font-size:23px;
  padding:2em;
}
#heading {
  font-size:21px;
}
#subheading {
  margin-left:3em;
  font-size:19px;
}
#text {
  font-size:17px;
}
</style>
"""


def six_toast(num):
    return num - 6 if num >= 6 else num
