<template>
    <div class="container header">
        <div class="header-logo">
            <img src="@/assets/logo.png" width="30" height="30"> 
            <div class="logo-title">
                <h5><a href="#">Game store</a></h5>
            </div>
        </div>
        <div class="navbar">
            <ul>
                <li><a href="#">Games</a></li>
                <li><a href="#">Community</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Support</a></li>
                <li><a href="#">Sign in</a></li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style>

.header {
    padding: 5px 0px;
    display: flex;
    color: #ffffff;
}

.header-logo {
    flex: 2;
    display: flex;
    align-items: center;
}

.logo-title {
    flex: 4;
    padding-top: 10px;
}

.logo-title h5 a {
    text-decoration: none;
    color: #ffffff;
}

.navbar {
    flex: 8;
}

.navbar ul{
    width: 100%;
    margin-top: 9px;
    padding: 0;
    list-style: none;
    display: flex;
}

.navbar li {
    flex: 1;
}

.navbar li:last-child {
    flex: 8;
    display: flex;
    justify-content: flex-end;
}

.navbar a{
    color: #ffffff;
    text-decoration: none;
    font-size: 16px;
    padding: 0px 10px;
}

</style>