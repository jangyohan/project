<template>
  <div>
    <AppHeader />
    <div class="col-lg-4 mx-auto">
      <div class="d-flex justify-content-center">
        <div class="py-4">
          <h1 class="h3 text-center">Create Feed</h1>
        </div>
      </div>
      <div class="form-group mt-4 bg-white">
        <label id="oneLineInput" class="text-info" for="oneLine">Title</label>
        <hr class="mb-1" />
        <textarea class="form-control border border-white" id="oneLine" rows="1"></textarea>
      </div>
      <div class="form-group mt-4 bg-white">
        <label id="oneLineInput" class="text-info" for="oneLine">Upload File</label>
        <hr />
        <div class="file_input">
          <input type="text" readonly="readonly" title="File Route" id="file_route" />
          <label>
            Search files
            <input
              class
              type="file"
              onchange="javascript:document.getElementById('file_route').value=this.value"
            />
          </label>
        </div>
      </div>
      <div class="form-group mt-4 bg-white">
        <label id="oneLineInput" class="text-info" for="oneLine">Content</label>
        <hr class="mb-1" />
        <textarea class="form-control border border-white" id="oneLine" rows="5"></textarea>
      </div>
      <div id="btn_group" class="d-flex flex-row-reverse">
        <button id="my_btn">Submit</button>
        <button id="my_btn">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FeedCreate",
  components: {},
};
</script>

<style>
</style>