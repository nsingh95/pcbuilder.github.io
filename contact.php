<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Contact us</title>
    <link rel="stylesheet" href="styles/contact_us.css" />
  </head>
  <body>
    <!-- header -->
    <?php include 'navigation.php' ;
      
    ?>

    <!-- main content -->
    <div class="flex-container">
      <div class="contact">
        <h2 style='color:white;margin-bottom:30px;'>Contact Us</h2>
        <p>
          
         <br />
          Email : <a href="#email">imnishantsingh902@gmail.com</a>
        </p>
        <br />
        <p>
          Office Timings : From 10Am - 6 Pm , MON-SAT.
        </p>
        <br />
        <p>Contact Us</p>
        <br />
        <p>
          Phone Number: 9304493099
        </p>
       
      </div>
      <div class="form">
        <h2 style='color:white;margin-bottom:30px;'>Feedback</h2>
        <label for="first_name"><b>Name</b></label>
        <input
          type="text"
          placeholder="Enter first name"
          name="first_name"
          id="first_name"
          required
        /><br />
        <label for="phone"><b>Phone Number</b></label>
        <input
          type="text"
          placeholder="Enter phone number"
          name="phone"
          id="phone"
          required
        /><br />
        <label for="email"><b>Email</b></label>
        <input
          type="text"
          placeholder="Enter Email"
          name="email"
          id="email"
          required
        /><br />
        <button type="button">Quotation Request </button>
        <p style='margin: 30px 0;'>
         
        </p>
      </div>
    </div>

    <!-- main content end -->

    <!-- footer -->
    <?php include 'footer.php' ?>
    
    </div>
  </body>
</html>
