<script lang="ts">
  import { enhance } from "$app/forms";
  import type { ActionData } from "./$types";
</script>

  <div class="max-w-[30vw] min-w-[500px] mx-auto mt-20 p-6">
  <h1 class="text-3xl font-bold mb-4">Are you sure you want to log out?</h1>
  <p class="text-gray-600 mb-6">Please confirm that you want to log out of your account.</p>

  <form method="POST" action="/logout" class="bg-white rounded-lg shadow-lg p-6 border border-gray-200 space-y-4" enctype="multipart/form-data" use:enhance>
    <div class="flex justify-between items-center">
      <button 
        type="submit" 
        class="bg-red-600 text-white py-2 px-4 rounded-lg hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
      >
        Log Out
      </button>

      <a 
        href="/" 
        class="text-blue-600 hover:text-blue-800 font-medium"
      >
        Cancel
      </a>
    </div>
  </form>
</div>
