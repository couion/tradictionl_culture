<script setup>

</script>
<template>
  <div class="titleNav">

    <div class="titleName">
      <slot></slot>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.titleNav {
  display: flex;
  // justify-content: center;
  align-items: center;
  height: 50px;
  border-left: 10px solid red;
  font-size: 20px;

  background-color: #595757;
  .titleName {
    height: 100%;
    width: 100px;
    text-align: center;
    line-height: 50px;
    background-color: #d2d2d2;
  }
}
</style>