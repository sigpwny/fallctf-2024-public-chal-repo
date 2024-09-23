<script lang="ts">
  import { enhance } from "$app/forms";
  import type { ActionData } from "./$types";

  export let form: ActionData;
</script>

<form method="post" class="bg-gray-200 p-4 font-mono max-w-sm mx-auto mt-[35vh] border border-gray-400" use:enhance>
  <input
    type="text"
    id="username"
    name="username"
    placeholder="Username"
    class="block mb-2 p-2 w-full border border-gray-400"
    required
  />
  
  <input
    type="password"
    id="password"
    name="password"
    placeholder="Password"
    class="block mb-2 p-2 w-full border border-gray-400"
    required
  />
  
  <button type="submit" class="block p-2 w-full bg-gray-400 text-black hover:bg-gray-500">Submit</button>

  {#if form?.error}
    <div class="mt-2 text-red-600">
      {@html form?.message}
    </div>
  {/if}
</form>