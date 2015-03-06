Title: Contact
sortorder: 99

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active"><i class="fa fa-map-marker"></i> Universidad de La Laguna (ULL)</li>
    </ul>
    <div class="content">
        <div class="row-fluid">
            <div class="vcard">
                <span class="fn">Pabellón de Gobierno</span><br>
                <span class="org">Universidad de La Laguna (ULL)<br>
                <p class="adr">
                    <span class="street-address">C/ Molinos de Agua, S/N<span><br>
                    <span class="postal-code">38200</span>, <span class="locality">San Cristóbal de La Laguna</span><br>
                    <span class="region">Santa Cruz de Tenerife</span><br>
                    <span class="country-name">España</span>
                </p>
                <i class="fa fa-envelope"></i><span class="email"><a href="mailto:email@example.com"> email@example.com</a></span><br>
                <i class="fa fa-phone"></i><span class="tel"><a href="tel:+34922319000"> (+34) 922 319 000</a></span>
            </div>
        </div>
    </div>
</div>

<h2>Contact Us</h2>

<noscript>
    <p>
        For further information, please dont hesitate to contact us by e-mail to 
        <a href="mailto:email@example.com"><i class="fa fa-envelope"></i> email@example.com</a>.
    </p>
</noscript>

<p class="jsonly">
    For further information, you can leave a message using the contact form below.
</p>
<div class="container-fluid jsonly">
    <div class="row">
        <div class="col-md-12">
            <div class="section">
                <ul class="nav nav-tabs header">
                    <li class="active">Contact form</li>
                </ul>
                <div class="content">
                    <div id="form-messages" role="alert"></div>
                    <form id="contact-form" method="post" action="php/mailer.php">
                        <div class="form-group" style="display: none">
                            <input type="text" class="form-control" id="honeypot" name="honeypot">
                        </div>
                        <div class="form-group">
                            <label class="">Your name: </label>
                            <input type="text" class="form-control" id="name" name="name" required>
                        </div>
                        <div class="form-group">
                            <label class="">Your e-mail address: </label>
                            <input type="email" class="form-control" id="email" name="email" required>
                        </div>
                        <div class="form-group">
                            <label class="">Message: </label>
                            <textarea class="form-control" rows="5" id="message" name="message" required></textarea>
                        </div>
                        <div class="checkbox">
                            <label>
                                <input type="checkbox" id="sendcopy" name="sendcopy" value="sendcopy"> Send yourself a copy
                            </label>
                        </div>
                        <button type="submit" class="btn btn-primary">Send</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
